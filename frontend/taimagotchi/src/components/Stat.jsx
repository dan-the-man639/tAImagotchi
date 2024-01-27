
import { useState, useEffect } from 'react';
import StatBar from './StatBar'

function Stat() {
  // const [statData, setStatData] = useState([]);
  const [hpSatiation, setHpSatiation] = useState(100);
  const [hpHydration, setHpHydration] = useState(100);
  const [hpEnergy, setHpEnergy] = useState(100);
  const [hpSanity, setHpSanity] = useState(100);

  const statData = [
    { Type: "Satiation", Stat: 95 },
    { Type: "Hydration", Stat: 90 },
    { Type: "Energy", Stat: 85 },
    { Type: "Sanity", Stat: 90 }
  ];
  // useEffect(() => {
  //   fetch("url")
  //     .then(response => response.json())
  //     .then(data => setStatData(data))
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
  