import './Option.css'
import { useState, useEffect } from 'react';

function Option() {
    const [option, setOption] = useState(['option 1', 'option 2', 'option 3', 'option 4']);

    // fetch request and save data
    const fetchData = async () => {
        const request = await fetch('http://127.0.0.1:8000/generate-options');

        const result = request.json();

        console.log(result);
        setOption(result);
    }

    //continously ask for fetch result
    useEffect(() => {
        fetchData();

        const intervalId = setInterval(() => {
            fetchData()
        }, 1000)

        return() => clearInterval(intervalId);
    }, [])

    //Handle on click that makes a post request
    const handleClick = () => {
        //loading variable
        setOption(['Loading...', 'Loading...', 'Loading...', 'Loading...']);

        //make post to get data
        fetch('url', {
            method: 'POST',
            headers: {
                Accept: 'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                firstParam: 'yourValue',
                secondParam: 'yourOtherValue',
            }),
        });

    }

    return (
        <div className='option-main'>
            <h1>Option box</h1>
            <div className="button-display">
                {option.map((item, index) => (
                    <button key={index}>{item}</button>
                ))}
            </div>
        </div>
    );
}

export default Option;
