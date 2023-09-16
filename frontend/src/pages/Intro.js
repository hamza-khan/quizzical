export default function Intro(props){
    return(
        <div className="intro">
            <h1>Quizzical</h1>
            <p>Enter the mind gym and grow your brain</p>
            <button className="action-button action-intro" onClick={props.startGame}>start quiz</button>
        </div>
    )
}