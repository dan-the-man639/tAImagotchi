import "./Stat.css";

import StatBar from "./StatBar";

function Stat({ statData }) {
  console.log("STATDATA:", statData)
  return (
    <div className="stat-bar">
      {statData.length > 3 && (
        <StatBar statItem={statData[0].Type} value={statData[0].Stat} />
      )}
      {statData.length > 3 && (
        <StatBar statItem={statData[1].Type} value={statData[1].Stat} />
      )}

      {statData.length > 3 && (
        <StatBar statItem={statData[2].Type} value={statData[2].Stat} />
      )}

      {statData.length > 3 && (
        <StatBar statItem={statData[3].Type} value={statData[3].Stat} />
      )}
    </div>
  );
}

export default Stat;
