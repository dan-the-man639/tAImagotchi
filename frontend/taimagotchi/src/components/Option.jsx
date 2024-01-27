import './Option.css'

function Option() {
    let option = ['option 1', 'option 2', 'option 3', 'option 4']

    return (
        <div className='option-main'>
            <h1>Option box</h1>
            <div className="button-display">
                {option.map((item, index) => (
                    <button key={index}>{item}</button>
                ))}
            </div>
        </div>
    );
}

export default Option;
