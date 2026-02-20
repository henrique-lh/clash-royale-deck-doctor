import type { Matchup } from "../../types/deckDoctor"
import { TrendingUp } from "lucide-react"

interface MatchupsProps {
  matchups: Matchup[]
}

const Matchups = ({ matchups }: MatchupsProps) => {
  const sortedMatchups = [...matchups].sort((a, b) => b.appearances - a.appearances)
  const maxAppearances = Math.max(...matchups.map(m => m.appearances), 1)

  return (
    <div className="glass-effect rounded-xl p-6 fade-in">
      <div className="flex items-center gap-3 mb-6">
        <TrendingUp className="text-blue-400" size={24} />
        <h3 className="text-xl font-bold text-white">Cartas Mais Encontradas</h3>
      </div>

      <div className="space-y-4">
        {sortedMatchups.slice(0, 8).map((matchup, idx) => {
          const percentage = (matchup.appearances / maxAppearances) * 100
          return (
            <div key={idx} className="group">
              <div className="flex items-center justify-between mb-2">
                <span className="font-semibold text-gray-200 group-hover:text-white transition">
                  {matchup.card}
                </span>
                <span className="text-sm font-bold text-blue-400">
                  {matchup.appearances} encontros
                </span>
              </div>
              <div className="w-full bg-gray-700/30 rounded-full h-2 overflow-hidden">
                <div
                  className="h-full bg-gradient-to-r from-blue-500 to-blue-600 rounded-full transition-all duration-500"
                  style={{ width: `${percentage}%` }}
                />
              </div>
            </div>
          )
        })}
      </div>

      {matchups.length > 8 && (
        <p className="text-xs text-gray-500 mt-4 text-center">
          + {matchups.length - 8} cartas adicionais
        </p>
      )}
    </div>
  )
}

export default Matchups
