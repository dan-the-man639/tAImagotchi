import './Interface.css'
import videoXD from '../assets/neutralloop.mp4'
import { ReactTyped } from "react-typed";

function Interface() {

    return (
        <div className='interface-display'>
            <div className='pet-display'>
                <h1>Here is your pet</h1>
                <video src={videoXD} autoPlay loop muted />
            </div>

            <div className='dialog-box'>
                <div>This is a paragraph</div>
                <ReactTyped
                    strings={[
                        "I'm a Full Stack Developer",
                        "I Love Software Development",
                        "I Love All My Subscribers",
                    ]}
                    typeSpeed={150}
                    backSpeed={100}
                    loop
                />
            </div>
        </div>
    );
}

export default Interface;
