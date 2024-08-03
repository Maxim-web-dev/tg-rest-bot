import { useEffect } from 'react'
import { useTelegram } from './hooks/useTelegram'
import Menu from './pages/menu/menu'

function App() {
  const { tg } = useTelegram()

  useEffect(() => {
    tg.ready()
  }, [])

  return (
   <Menu>
  
   </Menu>
  )
}

export default App
