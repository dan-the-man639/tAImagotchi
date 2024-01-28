import './Option.css';
import { useState, useEffect } from 'react';

function Option({ setStatData }) {
    const [option, setOption] = useState(['option 1', 'option 2', 'option 3', 'option 4']);
    const temp = ['option 1', 'option 2', 'option 3', 'option 4'];
    let second = 5 * 1000;

    const fetchDataOption = async () => {
        try {
            const response = await fetch('http://127.0.0.1:8000/generate-options');
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const result = await response.json();
            setOption(result);

            console.log(result);
        } catch (error) {
            console.error('Error:', error);
        }
    };

    const postData = async (optionSelected) => {
        try {
            const response = await fetch('http://127.0.0.1:8000/handle-action', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    "action": optionSelected
                }),
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            // Handle successful response, if needed
        } catch (error) {
            console.error('Error:', error);
        }
    };

  useEffect(() => {
    const intervalId = setInterval(() => {

      // generate new option
      fetchDataOption();
    }, second);

    return () => clearInterval(intervalId);
  }, []);
  
  const handleOnClick = (optionSelected) => {
    // make Post to send data
    postData(optionSelected);

  };

    return (
        <div className='option-main'>

            <div className="button-display">
                {option.map((item, index) => (
                    <button className='option-item' onClick={() => handleOnClick(item)} key={index}>{item}</button>
                ))}
            </div>
        </div>
    );
}

export default Option;
