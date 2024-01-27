import { useState, useEffect } from 'react';

//hp: current HP
//dif: newHP - current HP

function Stat({ statItem, value }) {
    const numParitions = 25;
    const imageBasePath = "/images/"; // Path relative to the public directory

    let imageName = statItem;
    let partitionValue = Math.floor(value / numParitions) * numParitions;

    imageName = imageBasePath + imageName + "_" + partitionValue + ".png";

    console.log(imageName);

    return (
        <div>
            <h2>{statItem}: {value}</h2>
            <div style={{ border: '1px solid #ccc', width: '300px', borderRadius: '5px', overflow: 'hidden' }}>
                <div
                    style={{
                        height: '20px',
                        backgroundColor: 'green',
                        transition: 'width 0.5s ease',
                    }}
                />
            </div>
            <img src={imageName} alt={`${statItem} stat bar`} />
        </div>
    );
}


export default Stat;
