
import { useState, useEffect } from 'react';
import StatBar from './StatBar'

function Stat() {
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
          console.log("data: ", data);
        })
        .catch(error => console.error('Error fetching data:', error));
    };

    // Call fetchStats immediately and then set an interval
    // fetchStats();
    const intervalId = setInterval(fetchStats, 1000); // Fetch every 1000 milliseconds (1 second)

    // Cleanup function to clear the interval when component unmounts
    return () => clearInterval(intervalId);
  }, []);



  return (
    <div className='stat-bar'>
      <StatBar statItem={statData[0].Type} value={statData[0].Stat}/>
      <StatBar statItem={statData[1].Type} value={statData[1].Stat}/>
      <StatBar statItem={statData[2].Type} value={statData[2].Stat}/>
      <StatBar statItem={statData[3].Type} value={statData[3].Stat}/>
    </div>
  );
  }
  
  export default Stat;
  