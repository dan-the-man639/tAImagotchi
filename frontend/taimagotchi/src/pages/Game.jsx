import Stat from '../components/Stat';
import Interface from '../components/Interface';
import './Game.css'
import Option from '../components/Option';
import TriggerBox from '../components/TriggerBox';
import { useState, useEffect } from 'react';


function Game() {
  let second = 4 * 1000;

  const [statData, setStatData] = useState([
    { Type: "Satiation", Stat: 100 },
    { Type: "Energy", Stat: 100 },
    { Type: "Happiness", Stat: 100 },
    { Type: "Intellect", Stat: 100 }
  ]);

  useEffect(() => {
    const fetchStats = () => {
      fetch("http://127.0.0.1:8000/get-stats")
        .then(response => response.json())
        .then(data => {
          setStatData(data);
          
        })
        .catch(error => console.error('Error fetching data:', error));
    };

    // Call fetchStats immediately and then set an interval
    // fetchStats();
    const intervalId = setInterval(fetchStats, second); // Fetch every 1000 milliseconds (1 second)

    // Cleanup function to clear the interval when component unmounts
    return () => clearInterval(intervalId);
  }, []);

  return (
    <div>
      <div className='main-container'>
        <div className='background-container'>
          <div className='background-image'></div>
        </div>

        <div className='main-interface'>
          <div className='top-panel'>
            <Stat statData = {statData}/>
            <Interface />
            <Option setStatData = {setStatData}/>
          </div>

          <div className='bottom-panel'>
            <TriggerBox />
          </div>
        </div>
      </div>

    </div>
  );
}

export default Game;
