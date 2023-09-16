import QuestionCard from "../components/QuestionCard"
import Questions from "../data/data"
import React from "react"


export default function QuestionAnswer(props){
    const [quiz, setQuiz] = React.useState(Questions)
    const [check, setCheck] = React.useState(false)
    const questions = quiz.map(quest=><QuestionCard
                                            quest={quest}
                                            key={quest.id}
                                            answerAQuestion={answerAQuestion}
                                            check={check}/>)


    function answerAQuestion(qId, aId){
        setQuiz(oldQuiz=>oldQuiz.map(quest=>quest.id===qId?
            {...quest, options:quest.options.map(opt=>opt.id===aId?
                {...opt, selected:true}:
                {...opt, selected:false})}:
            quest))
    }

    function checkAnswers(){
        setCheck(true)
    }

    function reset(){
        setCheck(false);
        props.setStart(false);

    }

    function getSumCorrect(total, quest){
        return (
            total+quest.options.map(
                opt=>(opt.correct&opt.selected)?1:0).reduce((tot, num)=>tot+num,0)
            )
    }

    const score = quiz.reduce(getSumCorrect, 0)
    const count = quiz.length
    return(
        <div className="question-answer">
            {questions}
            <div className="bottom-elements">
                {check?
                    <div>
                        <div className="the-question">You scored {score}/{count} correct answers</div>
                        <button className="action-button check-answers" onClick={reset}>Play again</button>
                    </div>
                    :
                    <button className="action-button check-answers" onClick={checkAnswers}>Check answers</button>}
            </div>
            
        </div>
    )
}