import { useState } from "react"
import { analyzePlayer } from "../api/deckDoctorApi"
import type { DeckDoctorResponse } from "../types/deckDoctor"
import Overview from "../components/dashboard/Overview"
import WinrateChart from "../components/dashboard/WinrateChart"
import SearchHeader from "../components/dashboard/SearchHeader"
import DiagnosisComponent from "../components/dashboard/Diagnosis"
import Matchups from "../components/dashboard/Matchups"
import { AlertCircle, RotateCcw } from "lucide-react"

const Home = () => {
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const [data, setData] = useState<DeckDoctorResponse | null>(null)
  const [currentTag, setCurrentTag] = useState<string | null>(null)

  const handleAnalyze = async (playerTag: string) => {
    setLoading(true)
    setError(null)

    try {
      const result = await analyzePlayer(playerTag)
      setData(result)
      setCurrentTag(playerTag)
    } catch (err: any) {
      const errorMsg = err.response?.data?.detail || err.message || "Falha ao analisar o jogador."
      console.error("API Error:", err)
      setError(errorMsg)
    } finally {
      setLoading(false)
    }
  }

  const handleReset = () => {
    setData(null)
    setCurrentTag(null)
    setError(null)
  }

  // Se não tem dados, mostra a tela de busca grande
  if (!data) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900">
        <SearchHeader onSearch={handleAnalyze} loading={loading} />

        {error && (
          <div className="fixed bottom-4 left-4 right-4 sm:left-auto sm:right-4 sm:w-96 glass-effect rounded-lg p-4 border-l-4 border-red-400 fade-in">
            <div className="flex gap-3">
              <AlertCircle className="text-red-400 flex-shrink-0 mt-0.5" size={20} />
              <div>
                <p className="font-semibold text-red-300">Erro</p>
                <p className="text-sm text-gray-300 mt-1">{error}</p>
              </div>
            </div>
          </div>
        )}
      </div>
    )
  }

  // Se tem dados, mostra o dashboard
  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 text-white">
      {/* Header compacto com campo de busca */}
      <div className="top-0 z-50 glass-effect border-b border-gray-700/50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
          <div className="flex items-center justify-between gap-4 mb-4">
            <div>
              <h1 className="text-2xl font-bold gradient-text">Deck Doctor</h1>
              <p className="text-xs text-gray-400">Analisando: {currentTag}</p>
            </div>
            <button
              onClick={handleReset}
              className="flex items-center gap-2 px-4 py-2 rounded-lg bg-gray-700/50 hover:bg-gray-600/50 transition-all text-sm font-semibold"
            >
              <RotateCcw size={16} />
              Nova Análise
            </button>
          </div>

          <SearchHeader onSearch={handleAnalyze} loading={loading} compact={true} />
        </div>
      </div>

      {/* Main Content */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {error && (
          <div className="mb-6 glass-effect rounded-lg p-4 border-l-4 border-red-400 fade-in">
            <div className="flex gap-3">
              <AlertCircle className="text-red-400 flex-shrink-0 mt-0.5" size={20} />
              <div>
                <p className="font-semibold text-red-300">Erro na análise</p>
                <p className="text-sm text-gray-300 mt-1">{error}</p>
              </div>
            </div>
          </div>
        )}

        {/* Stats Grid */}
        <Overview stats={data.stats} />

        {/* Main Charts */}
        <div className="grid lg:grid-cols-3 gap-6 mb-8">
          <div className="lg:col-span-2">
            <WinrateChart
              wins={data.stats.wins}
              losses={data.stats.losses}
            />
          </div>
          <div>
            <DiagnosisComponent diagnosis={data.diagnosis} />
          </div>
        </div>

        {/* Matchups */}
        {data.matchups.length > 0 && (
          <Matchups matchups={data.matchups} />
        )}
      </div>
    </div>
  )
}

export default Home
