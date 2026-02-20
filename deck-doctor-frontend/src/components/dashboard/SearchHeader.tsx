import { useState } from "react"
import { Search, ArrowRight } from "lucide-react"

interface SearchHeaderProps {
  onSearch: (playerTag: string) => void
  loading: boolean
  compact?: boolean
}

const SearchHeader = ({ onSearch, loading, compact = false }: SearchHeaderProps) => {
  const [playerTag, setPlayerTag] = useState("")

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    if (playerTag.trim()) {
      onSearch(playerTag)
    }
  }

  if (compact) {
    return (
      <form onSubmit={handleSubmit} className="slide-down">
        <div className="flex gap-2">
          <div className="flex-1 relative">
            <input
              type="text"
              placeholder="Novo jogador (#TAG)"
              value={playerTag}
              onChange={(e) => setPlayerTag(e.target.value)}
              maxLength={15}
              className="w-full px-4 py-2.5 rounded-lg bg-gray-800/60 border border-gray-700/60 focus:outline-none focus:border-blue-500 focus:ring-2 focus:ring-blue-500/20 transition-all text-sm"
            />
          </div>
          <button
            type="submit"
            disabled={loading}
            className="px-4 py-2.5 bg-gradient-to-r from-blue-500 to-blue-600 hover:from-blue-600 hover:to-blue-700 disabled:opacity-50 disabled:cursor-not-allowed rounded-lg font-semibold transition-all flex items-center gap-2"
          >
            <Search size={16} />
          </button>
        </div>
      </form>
    )
  }

  return (
    <div className="fade-in min-h-screen flex flex-col items-center justify-center px-4">
      <div className="text-center mb-12">
        <div className="inline-block mb-6">
          <div className="text-6xl font-bold mb-2">
            <span className="gradient-text">Deck Doctor</span>
          </div>
          <p className="text-gray-400 text-lg">Analise seu desempenho em Clash Royale</p>
        </div>
      </div>

      <form
        onSubmit={handleSubmit}
        className="w-full max-w-md"
      >
        <div className="glass-effect rounded-2xl p-8 shadow-2xl">
          <label className="block text-sm font-semibold text-gray-300 mb-4">
            Tag do Jogador
          </label>
          <div className="flex gap-3">
            <div className="flex-1 relative">
              <Search className="absolute left-4 top-3.5 text-gray-500" size={20} />
              <input
                type="text"
                placeholder="#PLAYER"
                value={playerTag}
                onChange={(e) => setPlayerTag(e.target.value.toUpperCase())}
                maxLength={15}
                className="w-full pl-12 pr-4 py-3 rounded-lg bg-gray-800/80 border border-gray-700 focus:outline-none focus:border-blue-400 focus:ring-2 focus:ring-blue-500/20 transition-all text-lg font-semibold"
                autoFocus
              />
            </div>
            <button
              type="submit"
              disabled={loading || !playerTag.trim()}
              className="px-8 py-3 bg-gradient-to-r from-blue-500 to-blue-600 hover:from-blue-600 hover:to-blue-700 disabled:opacity-50 disabled:cursor-not-allowed rounded-lg font-semibold transition-all flex items-center gap-2 whitespace-nowrap"
            >
              {loading ? "Analisando..." : "Analisar"}
              {!loading && <ArrowRight size={18} />}
            </button>
          </div>
          <p className="text-xs text-gray-500 mt-4 text-center">
            Digite sua tag sem # ou espaços
          </p>
        </div>
      </form>
    </div>
  )
}

export default SearchHeader
