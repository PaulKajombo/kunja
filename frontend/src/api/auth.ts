import { api } from './client'
import type { Token, UserLogin, UserOut, UserRegister } from './types'

export async function registerUser(payload: UserRegister): Promise<UserOut> {
  return api<UserOut>('/api/v1/auth/register', { method: 'POST', body: payload })
}

export async function loginUser(payload: UserLogin): Promise<Token> {
  return api<Token>('/api/v1/auth/login', { method: 'POST', body: payload })
}

export async function getMe(): Promise<UserOut> {
  return api<UserOut>('/api/v1/auth/me')
}