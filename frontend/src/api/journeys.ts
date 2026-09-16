import { api } from './client'
import type { Journey, JourneyList, JourneyOptions, JourneyStepUpdate } from './types'

export async function listJourneys(): Promise<JourneyList> {
  return api<JourneyList>('/api/v1/journeys')
}

export async function getJourney(id: number): Promise<Journey> {
  return api<Journey>(`/api/v1/journeys/${id}`)
}

export async function getJourneyOptions(): Promise<JourneyOptions> {
  return api<JourneyOptions>('/api/v1/journeys/options')
}

export interface CreateJourneyPayload {
  company_name: string
  origin_country: string
  target_country: string
  industry: string
  business_model: string
  business_description?: string
}

export async function createJourney(payload: CreateJourneyPayload): Promise<Journey> {
  return api<Journey>('/api/v1/journeys', { method: 'POST', body: payload })
}

export async function updateJourneyStep(
  journeyId: number,
  stepId: number,
  update: JourneyStepUpdate,
): Promise<Journey> {
  return api<Journey>(`/api/v1/journeys/${journeyId}/steps/${stepId}`, {
    method: 'PATCH',
    body: update,
  })
}