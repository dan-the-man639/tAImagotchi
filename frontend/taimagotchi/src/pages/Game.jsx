import Stat from '../components/Stat';
import Interface from '../components/Interface';
import './Game.css'
import Option from '../components/Option';

function Game() {

  return (
    <div className='main-container'>
      <div className='background-container'>
        <div className='background-image'></div>
      </div>

      <div className='main-interface'>
        <div className='top-panel'>
          <Stat />
          <Interface />
          <Option />
        </div>

        <div className='bottom-panel'>
          <div className='bottom-panel-inside'>
            This is a paragraph
          </div>
        </div>
      </div>
    </div>
  );
}

export default Game;
