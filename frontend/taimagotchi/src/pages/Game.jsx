import Stat from '../components/Stat';
import Interface from '../components/Interface';
import './Game.css'
import Option from '../components/Option';
import TriggerBox from '../components/TriggerBox';

import { useState, useEffect } from 'react';

function Game() {
  const [text, setText] = useState("");

  return (
    <div>
      <div className='main-container'>
        <div className='background-container'>
          <div className='background-image'></div>
        </div>

        <div className='main-interface'>
          <div className='top-panel'>
            <Stat />
            <Interface />
            <Option onTextChange={setText}/>
          </div>

          <div className='bottom-panel'>
            <TriggerBox text={text} setText={setText} /> {/* Pass text and setText to TriggerBox */}
          </div>
        </div>
      </div>

    </div>
  );
}

export default Game;
