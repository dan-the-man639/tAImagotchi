import './App.css';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Game from './pages/Game'
import Menu from './pages/Menu'

function App() {
  return (
    <div>
      <BrowserRouter>
        <Routes>
          <Route path='/menu' element={<Menu/>}></Route>
          <Route path='/' element={<Game/>}></Route>
        </Routes>
      </BrowserRouter>

      {/* <Game/> */}
    </div>
  );
}

export default App;
