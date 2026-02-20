import type { Diagnosis } from "../../types/deckDoctor"
import { AlertCircle, Lightbulb } from "lucide-react"

interface DaosisComponentProps {
  diagnosis: Diagnosis
}

const DiagnosisComponent = ({ diagnosis }: DaosisComponentProps) => {
  return (
    <div className="glass-effect rounded-xl p-6 fade-in">
      <div className="mb-6">
        <div className="flex items-center gap-3 mb-4">
          <AlertCircle className="text-amber-400" size={24} />
          <h3 className="text-xl font-bold text-white">Diagnóstico do Deck</h3>
        </div>
        <p className="text-sm font-semibold text-amber-300 bg-amber-500/10 w-fit px-3 py-1 rounded-full">
          {diagnosis.deck_type}
        </p>
      </div>

      {diagnosis.problems.length > 0 && (
        <div className="mb-6">
          <div className="flex items-center gap-2 mb-3">
            <AlertCircle className="text-red-400" size={20} />
            <h4 className="font-semibold text-white">Problemas Identificados</h4>
          </div>
          <ul className="space-y-2">
            {diagnosis.problems.map((problem, idx) => (
              <li key={idx} className="flex gap-3 text-gray-300">
                <span className="text-red-400 font-bold mt-0.5">•</span>
                <span>{problem}</span>
              </li>
            ))}
          </ul>
        </div>
      )}

      {diagnosis.recommendations.length > 0 && (
        <div>
          <div className="flex items-center gap-2 mb-3">
            <Lightbulb className="text-green-400" size={20} />
            <h4 className="font-semibold text-white">Recomendações</h4>
          </div>
          <ul className="space-y-2">
            {diagnosis.recommendations.map((rec, idx) => (
              <li key={idx} className="flex gap-3 text-gray-300">
                <span className="text-green-400 font-bold mt-0.5">✓</span>
                <span>{rec}</span>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  )
}

export default DiagnosisComponent
