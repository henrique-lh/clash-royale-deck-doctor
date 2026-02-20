import axios from "axios"

const api = axios.create({
  baseURL: "http://localhost:8000", // backend
})

api.interceptors.response.use(
  response => response,
  error => {
    if (!error.response) {
      console.error("Network Error:", error)
      throw new Error("Unable to connect to the server. Make sure the backend is running on http://localhost:8000")
    }
    return Promise.reject(error)
  }
)

export const analyzePlayer = async (playerTag: string) => {
  const refres_response = await api.post(`/players/${encodeURIComponent(playerTag)}/refresh`)
  if (refres_response.status !== 200) {
    throw new Error(`API Error: ${refres_response.status} ${refres_response.statusText}`)
  }
  const analyze_data = await api.get(`/players/${encodeURIComponent(playerTag)}/analysis`)
  return analyze_data.data
}
