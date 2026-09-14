const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

export async function api<T>(path: string, options: RequestInit = {}): Promise<T> {
  const res = await fetch(`${API_URL}${path}`, {
    headers: { 'Content-Type': 'application/json', ...options.headers },
    ...options,
  })

  if (!res.ok) {
    const error = await res.json().catch(() => ({ detail: `Error ${res.status}` }))
    throw new Error(error.detail || `Error ${res.status}`)
  }

  return res.json() as Promise<T>
}

export interface Category {
  key: string
  name: string
  regulation: string
  question_count: number
}

export interface Country {
  code: string
  name: string
  flag: string
  categories: Category[]
}

export interface Question {
  id: string
  question: string
  answer_type: string
  critical: boolean
  requirement: string
  resource?: string
}

export interface Checklist {
  id: number
  origin_country: string
  target_country: string
  business_type: string
  industry: string
  company_name: string
  compliance_score: number | null
  compliance_level: string | null
  status: string
  created_at: string
}

export interface SubmitResult {
  checklist_id: number
  compliance_score: number
  compliance_level: string
  category_scores: Record<string, CategoryScore>
  gaps: Gap[]
  critical_gaps_count: number
  status: string
}

export interface CategoryScore {
  score: number
  passed: number
  total: number
  name: string
  regulation: string
}

export interface Gap {
  question_id: string
  category: string
  question: string
  requirement: string
  critical: boolean
  resource?: string
}