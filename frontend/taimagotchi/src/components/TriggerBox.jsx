import "./TriggerBox.css";
import { ReactTyped } from "react-typed";
import { useState, useEffect } from "react";

function TriggerBox() {
    const [text, setText] = useState("Hello, my nane is Tai, I am a Taimagotchi. Please take care of me!");
    let second = 20 * 1000;

    const fetchDataPrompt = async () => {
        try {
            const response = await fetch('http://127.0.0.1:8000/generate-trigger');
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const result = await response.json();

            console.log(result);
            setText(result);
        } catch (error) {
            console.error('Error:', error);
        }
    };

    useEffect(() => {
        const intervalId = setInterval(() => {
            fetchDataPrompt();
        }, second);

        return () => clearInterval(intervalId);
    }, []);

  return (
    <div class="parent">
      <div class="background">
        <div class="text">
            <ReactTyped strings={[text]} typeSpeed={50} />
        </div>
      </div>
    </div>
  );
}

export default TriggerBox;
