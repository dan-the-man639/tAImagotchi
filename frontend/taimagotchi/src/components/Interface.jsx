import './Interface.css';
import { useState, useEffect } from 'react';
import Neutral1 from '../assets/neutral1.png';
import Neutral2 from '../assets/neutral2.png';
import Happy1 from '../assets/happy1.png';
import Happy2 from '../assets/happy2.png';
import Sad1 from '../assets/sad1.png';
import Sad2 from '../assets/sad2.png';

function Interface() {
  const [currentImage, setCurrentImage] = useState(0);
  const [mood, setMood] = useState('neutral'); // Default mood is neutral
  const imageSources = getImageSources(mood);
  const [data, setData] = useState(null); //for storing api data

  useEffect(() => {
    const intervalId = setInterval(() => {
      setCurrentImage((prevImage) => (prevImage + 1) % imageSources.length);
    }, 1000); // Change image every 1000 milliseconds (1 second)

    return () => clearInterval(intervalId); // Cleanup the interval on component unmount
  }, [imageSources]); // Update the effect when mood changes

  // Function to get image sources based on mood-----------
  function getImageSources(mood) {
    switch (mood) {
      case 'happy':
        return [Happy1, Happy2];
      case 'sad':
        return [Sad1, Sad2];
      default:
        return [Neutral1, Neutral2];
    }
  }

  // Function to handle mood change-------------------------
  const handleMoodChange = (newMood) => {
    if(newMood == 0){
      setMood('happy');
    } else if (newMood == 2){
      setMood('sad');
    } else {
      setMood('neutral');
    }

    setCurrentImage(0);
  };

 // Function that grabes api---------------
  const fetchData = async () => {
    try {
      const response = await fetch('http://127.0.0.1:8000/get-state');
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const result = await response.json();
      // console.log(result);

      // Check if the result indicates a change in mood
      if (result && result.is_alive && result.emotion !== result.emotion) {
        handleMoodChange(result.mood);
      }

      setData(result);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  //grabs the api continously and stores it into a useState-----------------
  useEffect(() => {
    fetchData();

    const intervalId = setInterval(() => {
      fetchData();
    }, 1000);

    return () => clearInterval(intervalId);
  }, []);

    //if result change than handle the state
    

  return (
    <div className='interface-display'>
      <div className='pet-display'>
        <h1>Here is your pet</h1>
        <img src={imageSources[currentImage]} alt={`Image ${currentImage + 1}`} />
      </div>
      
    </div>
  );
}

export default Interface;
