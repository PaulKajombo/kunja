const API_URL = import.meta.env.VITE_API_URL || ''
const AUTH_TOKEN_KEY = 'kunja_token'

export function getToken(): string | null {
  return localStorage.getItem(AUTH_TOKEN_KEY)
}

export function setToken(token: string | null) {
  if (token) localStorage.setItem(AUTH_TOKEN_KEY, token)
  else localStorage.removeItem(AUTH_TOKEN_KEY)
}

export class ApiError extends Error {
  status: number
  constructor(status: number, message: string) {
    super(message)
    this.status = status
  }
}

interface ApiOptions {
  method?: string
  headers?: Record<string, string>
  body?: unknown
}

function buildFetchOptions(options: ApiOptions): RequestInit {
  const headers: Record<string, string> = { ...options.headers }
  const token = getToken()
  if (token) headers['Authorization'] = `Bearer ${token}`
  const init: RequestInit = { method: options.method, headers }
  const body = options.body
  if (body instanceof FormData) {
    init.body = body
  } else if (body !== undefined && body !== null) {
    init.body = typeof body === 'string' ? body : JSON.stringify(body)
    if (headers['Content-Type'] === undefined) {
      headers['Content-Type'] = 'application/json'
    }
  }
  return init
}

function extractDetail(data: unknown): string {
  if (typeof data !== 'object' || data === null) return ''
  const obj = data as Record<string, unknown>
  const detail = obj.detail
  if (typeof detail === 'string') return detail
  if (Array.isArray(detail)) {
    return detail
      .map((d) => {
        if (typeof d === 'object' && d !== null && 'msg' in d) {
          return String((d as { msg: unknown }).msg)
        }
        return String(d)
      })
      .join(', ')
  }
  return ''
}

export async function api<T>(path: string, options: ApiOptions = {}): Promise<T> {
  const res = await fetch(`${API_URL}${path}`, buildFetchOptions(options))

  if (!res.ok) {
    let message = `Error ${res.status}`
    try {
      const data = await res.json()
      message = extractDetail(data) || message
    } catch {
      /* keep default message */
    }
    throw new ApiError(res.status, message)
  }

  return res.json() as Promise<T>
}

export async function apiVoid<T = never>(path: string, options: ApiOptions = {}): Promise<T> {
  const res = await fetch(`${API_URL}${path}`, buildFetchOptions(options))

  if (!res.ok) {
    let message = `Error ${res.status}`
    try {
      const data = await res.json()
      message = extractDetail(data) || message
    } catch {
      /* keep default */
    }
    throw new ApiError(res.status, message)
  }
  if (res.status === 204) return undefined as unknown as T
  return res.json() as Promise<T>
}