export interface Stats {
  total_battles: number
  wins: number
  losses: number
  winrate: number
  avg_elixir: number
  avg_elixir_leaked: number
}

export interface Matchup {
  card: string
  appearances: number
}

export interface Diagnosis {
  deck_type: string
  problems: string[]
  recommendations: string[]
}

export interface DeckDoctorResponse {
  stats: Stats
  matchups: Matchup[]
  diagnosis: Diagnosis
}
