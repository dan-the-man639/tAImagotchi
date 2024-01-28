import "./TriggerBox.css";
import { ReactTyped } from "react-typed";
import { useState, useEffect } from "react";

function TriggerBox({ text, setText }) {
    const text2 = "hello";
  return (
    <div class="parent">
      <div class="background">
        <div class="text">
            {/* <ReactTyped strings={[text2]} typeSpeed={40} /> */}
        </div>
      </div>
    </div>
  );
}

export default TriggerBox;
