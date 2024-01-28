import './Menu.css'
import { useNavigate } from 'react-router-dom';

function Menu() {
  const handleQuit = () => {
    window.open("about:blank", "_self");
    window.close();
}

let navigate = useNavigate();

  const goToHomePage = () => {
    navigate('/game');
  };

  return (
    <>

    
    <div class="titlediv">
        <h1 class="title">tAImagotchi</h1>
    </div >

    <div class="maintama" >
      <img src={require('../assets/mainmenu-tama.png')} width={250}/>
    </div>

    <div class="container"> 
        <div class="bubble">
          <span style={{"--i":11}}></span>
          <span style={{"--i":9}}></span>
          <span style={{"--i":17}}></span>
          <span style={{"--i":21}}></span>
          <span style={{"--i":52}}></span>
          <span style={{"--i":10}}></span>
          <span style={{"--i":20}}></span>
          <span style={{"--i":31}}></span>
          <span style={{"--i":15}}></span>
          <span style={{"--i":8}}></span>
          <span style={{"--i":22}}></span>
          <span style={{"--i":6}}></span>
          <span style={{"--i":12}}></span>
          <span style={{"--i":42}}></span>
          <span style={{"--i":23}}></span>
          <span style={{"--i":19}}></span>
         

        </div>

      </div>

    <div class="options">
      <div>
        <button class="play" onClick={goToHomePage}>PLAY</button> 
        <img class="playarrow" src={require('../assets/arrowpoint.png')} width={24}/>
      </div>
      <div>
        <button class="settings">SETTINGS</button>
        <img class="settingarrow" src={require('../assets/arrowpoint.png')} width={24}/>
        </div>
      <div>
        <button class="quit" onClick={handleQuit}>QUIT</button>
        <img class="quitarrow" src={require('../assets/arrowpoint.png')} width={24}/>
        </div>
    </div>
    <div>

     
      
    </div>
    </>
  );
}

export default Menu;
