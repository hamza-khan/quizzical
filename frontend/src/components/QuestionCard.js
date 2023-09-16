import OptionCard from "./OptionCard";

export default function QuestionCard(props){
    const optionsElements = props.quest.options.map(opt=><OptionCard opt={opt} key={opt.id} answerAQuestion={props.answerAQuestion} qId={props.quest.id} check={props.check}/>)
    return(
        <div>
            <div className="the-question">{props.quest.question}</div>
            <div className="the-options">{optionsElements}</div>
        </div>
    )
}