
import { useState, useEffect } from 'react';

//hp: current HP
//dif: newHP - current HP

function Stat({ statItem, hp, onSetHp, dif }) {
    //const [hp, setHp] = useState(100); // Initial HP value
    const decreaseRate = 1; // HP decrease rate per minute
    const increaseAmount = 2; // HP increase amount when the button is clicked
    const[currentHp, setCurrentHp] = useState(hp + dif);
    //const mockReturned = [
    //     {hunger: 95},
    //     {health: 90},
    //     {thrist: 85},
    //     {happiness: 80}
    //   ]



    useEffect(() => {
            const interval = setInterval(() => {
                // Decrease HP every minute
                onSetHp((prevHp) => (prevHp > currentHp ? prevHp - decreaseRate : currentHp));
            }, 1000); // 60000 milliseconds = 1 minute

            return () => clearInterval(interval);
    }, []);

    useEffect(() => {
        setCurrentHp(hp + dif);
        onSetHp(hp + dif);
    }, [hp, dif])

    return (
        <div>
            <h2>{statItem}: {currentHp}</h2>
            <div style={{ border: '1px solid #ccc', width: '300px', borderRadius: '5px', overflow: 'hidden' }}>
                <div
                    style={{
                        width: `${currentHp}%`,
                        height: '20px',
                        backgroundColor: 'green',
                        transition: 'width 0.5s ease',
                    }}
                />
            </div>
        </div>
    );
}

export default Stat;
