import "./TriggerBox.css";
import { ReactTyped } from "react-typed";
import { useState, useEffect } from "react";

function TriggerBox({ text, setText }) {

  return (
    <div class="parent">
      <div class="background">
        <div class="text">
            <ReactTyped strings={[text]} typeSpeed={40} />
        </div>
      </div>
    </div>
  );
}

export default TriggerBox;
