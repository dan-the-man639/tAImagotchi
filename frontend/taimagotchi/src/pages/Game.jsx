import Stat from '../components/Stat';
import Interface from '../components/Interface';
import './Game.css'

function Game() {

  return (
    <div className='main-interface'>
      
      <div className='left-panel'>
        <Stat />
      </div>
      
      <div className='right-panel'>
        <Interface />
      </div>
    </div>
  );
}

export default Game;
