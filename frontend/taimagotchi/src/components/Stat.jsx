
import { useState, useEffect } from 'react';
import StatBar from './StatBar'

function Stat() {
  const [statData, setStatData] = useState([
    { Type: "Satiation", Stat: 100 },
    { Type: "Hydration", Stat: 100 },
    { Type: "Energy", Stat: 100 },
    { Type: "Sanity", Stat: 100 }
  ]);
  const [hpSatiation, setHpSatiation] = useState(100);
  const [hpHydration, setHpHydration] = useState(100);
  const [hpEnergy, setHpEnergy] = useState(100);
  const [hpSanity, setHpSanity] = useState(100);

  // useEffect(() => {
  //   fetch("http://127.0.0.1:8000/get-stats")
  //     .then(response => response.json())
  //     .then(data => {
  //       setStatData(data);
  //       console.log("data: ", data);
  //     })
  //     .catch(error => console.error('Error fetching data:', error));
  // }, []);


  return (
    <div className='stat-bar'>
      <StatBar statItem={statData[0].Type} hp={hpSatiation}  onSetHp={setHpSatiation} dif={statData[0].Stat - hpSatiation }/>
      <StatBar statItem={statData[1].Type} hp={hpHydration}  onSetHp={setHpHydration} dif={statData[1].Stat - hpHydration}/>
      <StatBar statItem={statData[2].Type} hp={hpEnergy}  onSetHp={setHpEnergy} dif={statData[2].Stat - hpEnergy}/>
      <StatBar statItem={statData[3].Type} hp={hpSanity}  onSetHp={setHpSanity} dif={statData[3].Stat - hpSanity}/>
    </div>
  );
  }
  
  export default Stat;
  