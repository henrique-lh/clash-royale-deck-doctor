import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, Cell } from "recharts"
import { Swords } from "lucide-react"

interface Props {
  wins: number
  losses: number
}

const WinrateChart = ({ wins, losses }: Props) => {
  const total = wins + losses
  const winrate = total > 0 ? ((wins / total) * 100).toFixed(1) : 0

  const data = [
    { name: "Vitórias", value: wins },
    { name: "Derrotas", value: losses },
  ]

  const COLORS = ["#10b981", "#ef4444"]

  return (
    <div className="glass-effect rounded-xl p-6 fade-in">
      <div className="flex items-center justify-between mb-6">
        <div className="flex items-center gap-3">
          <Swords className="text-green-400" size={24} />
          <h2 className="text-xl font-bold text-white">Resultado das Batalhas</h2>
        </div>
        <div className="text-right">
          <p className="text-3xl font-bold bg-gradient-to-r from-green-400 to-blue-400 bg-clip-text text-transparent">
            {winrate}%
          </p>
          <p className="text-xs text-gray-400">taxa de vitória</p>
        </div>
      </div>

      <ResponsiveContainer width="100%" height={300}>
        <BarChart data={data} margin={{ top: 20, right: 30, left: 0, bottom: 0 }}>
          <XAxis dataKey="name" stroke="#94a3b8" style={{ fontSize: "14px" }} />
          <YAxis stroke="#94a3b8" style={{ fontSize: "14px" }} />
          <Tooltip
            contentStyle={{
              backgroundColor: "#1e293b",
              border: "1px solid #475569",
              borderRadius: "8px",
              color: "#f1f5f9",
            }}
            cursor={{ fill: "rgba(59, 130, 246, 0.1)" }}
          />
          <Bar dataKey="value" radius={[8, 8, 0, 0]}>
            {data.map((_, index) => (
              <Cell key={`cell-${index}`} fill={COLORS[index]} />
            ))}
          </Bar>
        </BarChart>
      </ResponsiveContainer>

      <div className="grid grid-cols-2 gap-4 mt-6 pt-6 border-t border-gray-700">
        <div className="text-center">
          <p className="text-2xl font-bold text-green-400">{wins}</p>
          <p className="text-sm text-gray-400">Vitórias</p>
        </div>
        <div className="text-center">
          <p className="text-2xl font-bold text-red-400">{losses}</p>
          <p className="text-sm text-gray-400">Derrotas</p>
        </div>
      </div>
    </div>
  )
}

export default WinrateChart
