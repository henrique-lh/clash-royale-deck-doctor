import type { Stats } from "../../types/deckDoctor"
import { Target, Swords, TrendingUp, Zap } from "lucide-react"

interface Props {
  stats: Stats
}

const Overview = ({ stats }: Props) => {
  const winrateColor = stats.winrate >= 55 ? "text-green-400" : stats.winrate >= 50 ? "text-blue-400" : "text-amber-400"
  const elixirColor = stats.avg_elixir_leaked > 5 ? "text-red-400" : stats.avg_elixir_leaked > 3 ? "text-amber-400" : "text-green-400"

  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-6 gap-4 mb-8 fade-in">
      <StatCard
        icon={Target}
        label="Batalhas"
        value={stats.total_battles}
        color="from-blue-500/20 to-blue-600/20"
        iconColor="text-blue-400"
      />
      <StatCard
        icon={Swords}
        label="Vitórias"
        value={stats.wins}
        color="from-green-500/20 to-green-600/20"
        iconColor="text-green-400"
      />
      <StatCard
        icon={Swords}
        label="Derrotas"
        value={stats.losses}
        color="from-red-500/20 to-red-600/20"
        iconColor="text-red-400"
      />
      <StatCard
        icon={TrendingUp}
        label="Taxa de Vitória"
        value={`${stats.winrate.toFixed(1)}%`}
        color="from-purple-500/20 to-purple-600/20"
        iconColor={winrateColor}
      />
      <StatCard
        icon={Zap}
        label="Elixir Médio"
        value={stats.avg_elixir.toFixed(1)}
        color="from-amber-500/20 to-amber-600/20"
        iconColor="text-amber-400"
      />
      <StatCard
        icon={Zap}
        label="Elixir Desperdiçado"
        value={stats.avg_elixir_leaked.toFixed(1)}
        color="from-orange-500/20 to-orange-600/20"
        iconColor={elixirColor}
      />
    </div>
  )
}

const StatCard = ({ 
  icon: Icon, 
  label, 
  value, 
  color,
  iconColor 
}: { 
  icon: any
  label: string
  value: any
  color: string
  iconColor: string
}) => (
  <div className={`glass-effect rounded-xl p-4 text-center group hover:scale-105 transition-transform duration-300 bg-gradient-to-br ${color}`}>
    <div className="flex justify-center mb-3">
      <Icon className={`${iconColor} group-hover:scale-110 transition-transform`} size={24} />
    </div>
    <p className="text-gray-400 text-xs font-medium uppercase tracking-wide mb-2">{label}</p>
    <p className="text-2xl md:text-3xl font-bold text-white">{value}</p>
  </div>
)

export default Overview
