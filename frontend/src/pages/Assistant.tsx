import { useState } from 'react'

import { api } from '../lib/api'

interface Message {
  role: 'user' | 'assistant'
  text: string
}

export default function Assistant() {
  const [messages, setMessages] = useState<Message[]>([
    {
      role: 'assistant',
      text: "Hi! I'm Kunja. Ask me anything about cross-border market entry between Malawi and Zambia — trade requirements, compliance steps, documents, regulations, or what to do next.",
    },
  ])
  const [input, setInput] = useState('')
  const [loading, setLoading] = useState(false)

  const sendMessage = async (e: React.FormEvent) => {
    e.preventDefault()
    if (!input.trim() || loading) return

    const question = input.trim()
    setInput('')
    setMessages((prev) => [...prev, { role: 'user', text: question }])
    setLoading(true)

    try {
      // Use the global ask endpoint (journey_id = null → whole-journey context)
      // We'll try to find an existing journey first, then ask without step context
      let journeys: { journeys: { id: number }[] } = { journeys: [] }
      try {
        journeys = await api<{ journeys: { id: number }[] }>('/api/v1/journeys')
      } catch {}

      const journeyId = journeys.journeys?.[0]?.id

      if (journeyId) {
        const res = await api<{ answer: string }>(`/api/v1/journeys/${journeyId}/ask`, {
          method: 'POST',
          body: JSON.stringify({ question }),
        })
        setMessages((prev) => [...prev, { role: 'assistant', text: res.answer }])
      } else {
        setMessages((prev) => [
          ...prev,
          {
            role: 'assistant',
            text: "You don't have any journeys yet. Create a journey first and I'll be able to answer questions specific to your business context. Click 'Start Journey' to begin.",
          },
        ])
      }
    } catch (err) {
      setMessages((prev) => [
        ...prev,
        {
          role: 'assistant',
          text: `Sorry, I couldn't process that: ${err instanceof Error ? err.message : 'Unknown error'}`,
        },
      ])
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="chat-container">
      <div className="flex-between mb-3">
        <div>
          <h1 style={{ fontSize: '1.4rem', fontWeight: 700, marginBottom: '4px' }}>AI Assistant</h1>
          <p className="text-sm text-muted">Ask Kunja about market entry, compliance, and next steps</p>
        </div>
      </div>

      <div className="card" style={{ padding: '24px' }}>
        <div className="chat-messages">
          {messages.map((msg, i) => (
            <div key={i} className={`chat-message ${msg.role}`}>
              {msg.text}
            </div>
          ))}
          {loading && (
            <div className="chat-message assistant">
              <span className="spinner spinner-dark" />
            </div>
          )}
        </div>

        <form onSubmit={sendMessage} className="chat-input-bar">
          <input
            type="text"
            placeholder="Ask about trade requirements, compliance, or what to do next..."
            value={input}
            onChange={(e) => setInput(e.target.value)}
            disabled={loading}
          />
          <button className="btn" type="submit" disabled={loading || !input.trim()}>
            Send
          </button>
        </form>
      </div>
    </div>
  )
}
