import {
  createContext,
  useCallback,
  useContext,
  useEffect,
  useMemo,
  useState,
} from 'react'
import { getMe, loginUser, registerUser } from '../api/auth'
import { getToken, setToken } from '../api/client'
import type { UserLogin, UserOut, UserRegister } from '../api/types'

interface AuthContextValue {
  user: UserOut | null
  loading: boolean
  login: (credentials: UserLogin) => Promise<void>
  register: (profile: UserRegister) => Promise<void>
  logout: () => void
}

const AuthContext = createContext<AuthContextValue | null>(null)

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [user, setUser] = useState<UserOut | null>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    let cancelled = false
    const token = getToken()
    if (!token) {
      setLoading(false)
      return
    }
    getMe()
      .then((u) => {
        if (!cancelled) setUser(u)
      })
      .catch(() => {
        setToken(null)
        if (!cancelled) setUser(null)
      })
      .finally(() => {
        if (!cancelled) setLoading(false)
      })
    return () => {
      cancelled = true
    }
  }, [])

  const login = useCallback(async (credentials: UserLogin) => {
    const { access_token } = await loginUser(credentials)
    setToken(access_token)
    setUser(await getMe())
  }, [])

  const register = useCallback(async (profile: UserRegister) => {
    await registerUser(profile)
    const { access_token } = await loginUser({
      email: profile.email,
      password: profile.password,
    })
    setToken(access_token)
    setUser(await getMe())
  }, [])

  const logout = useCallback(() => {
    setToken(null)
    setUser(null)
  }, [])

  const value = useMemo(
    () => ({ user, loading, login, register, logout }),
    [user, loading, login, register, logout],
  )

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>
}

export function useAuth(): AuthContextValue {
  const ctx = useContext(AuthContext)
  if (!ctx) throw new Error('useAuth must be used within an AuthProvider')
  return ctx
}