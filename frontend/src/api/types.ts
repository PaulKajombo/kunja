/* ─── Categories / Countries (legacy compliance) ──────────────────── */

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

/* ─── Journeys ───────────────────────────────────────────────────── */

export interface JourneyOptions {
  countries: { key: string; name: string; flag: string }[]
  industries: string[]
  business_models: { key: string; label: string; description: string }[]
}

export interface JourneyStep {
  id: number
  step_number: number
  title: string
  slug: string
  description: string | null
  why_needed: string | null
  authority: string | null
  documents_needed: string[]
  instructions: string | null
  estimated_cost: string | null
  estimated_timeline: string | null
  official_source: string | null
  status: string
  user_notes: string | null
  depends_on: number[]
}

export interface JourneyPhase {
  id: number
  phase_number: number
  name: string
  description: string
  steps: JourneyStep[]
}

export interface JourneyProgress {
  total_steps: number
  completed_steps: number
  in_progress_steps: number
  blocked_steps: number
  percentage: number
  next_step_id: number | null
  next_step_title: string | null
}

export interface Journey {
  id: number
  company_name: string
  origin_country: string
  target_country: string
  industry: string
  business_model: string
  business_model_label: string
  business_description: string | null
  status: string
  created_at: string | null
  phases: JourneyPhase[]
  progress: JourneyProgress
}

export interface JourneyList {
  journeys: Journey[]
}

export interface JourneyStepUpdate {
  status?: string
  user_notes?: string
}

/* ─── Documents ──────────────────────────────────────────────────── */

export type DocumentStatus =
  | 'MISSING'
  | 'UPLOADED'
  | 'IN_REVIEW'
  | 'VERIFIED'
  | 'REJECTED'

export interface Document {
  id: number
  journey_id: number | null
  step_id: number | null
  requirement: string | null
  filename: string
  file_type: string
  file_size: number
  storage_path: string
  status: DocumentStatus
  created_at: string | null
  updated_at: string | null
}

export interface DocumentList {
  documents: Document[]
  total: number
}

export interface DocumentDelete {
  deleted: boolean
  id: number
}

/* ─── Ask / Misc ─────────────────────────────────────────────────── */

export interface AskResponse {
  answer: string
  step_id: number | null
}

/* ─── Auth ───────────────────────────────────────────────────────── */

export interface UserOut {
  id: number
  email: string
  full_name: string
  country: string
  created_at: string | null
}

export interface Token {
  access_token: string
  token_type: string
}

export interface UserRegister {
  email: string
  password: string
  full_name: string
  country: string
}

export interface UserLogin {
  email: string
  password: string
}