import './Interface.css'
import videoXD from '../assets/neutralloop.mp4'
import Typed from "react-typed";

function Interface() {

    return (
        <>
            <div className='pet-display'>
                <h1>Here is your pet</h1>
                <video src={videoXD} autoPlay loop muted />
            </div>

            <div className='dialog-box'>
                <div>This is a paragraph</div>
                <Typed
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
        </>
    );
}

export default Interface;
