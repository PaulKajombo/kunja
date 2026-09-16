import { Component } from 'react'

interface Props {
  children: React.ReactNode
}
interface State {
  hasError: boolean
  error: Error | null
}

export default class ErrorBoundary extends Component<Props, State> {
  state: State = { hasError: false, error: null }

  static getDerivedStateFromError(error: Error): State {
    return { hasError: true, error }
  }

  reset = () => this.setState({ hasError: false, error: null })

  render() {
    if (this.state.hasError) {
      return (
        <div style={{
          minHeight: '100vh',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          padding: 24,
        }}>
          <div className="card" style={{ maxWidth: 480, textAlign: 'center' }}>
            <h2 style={{ marginBottom: 8 }}>Something went wrong</h2>
            <p className="text-sm text-muted" style={{ marginBottom: 16 }}>
              {this.state.error?.message ?? 'An unexpected error occurred.'}
            </p>
            <button className="btn" onClick={() => { this.reset(); window.location.reload() }}>
              Reload page
            </button>
          </div>
        </div>
      )
    }
    return this.props.children
  }
}