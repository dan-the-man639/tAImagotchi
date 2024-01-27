import './Interface.css'
import videoXD from '../assets/neutralloop.mp4'
import Typed from "react-typed";

function Interface() {

    return (
        <div className='interface-display'>
            <div className='pet-display'>
                <h1>Here is your pet</h1>
                <video src={videoXD} autoPlay loop muted />
            </div>

            
        </div>
    );
}

export default Interface;
