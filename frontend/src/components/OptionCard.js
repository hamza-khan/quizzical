import React from "react"
export default function OptionCard(props){
    let classes = "the-option"

    if (props.check){
        if (props.opt.correct){
            classes = `${classes} correct`
        }
        if (props.opt.selected & !props.opt.correct){
            classes = `${classes} wrong`
        }
        if(!props.opt.selected & !props.opt.correct){
            classes = `${classes} not-selected`
        }
    }else{
        if (props.opt.selected){
            classes = `${classes} selected`
        }else{
            classes = `${classes} not-selected`
        }
    }
        
    function doNothing(){
        //pass
    }



    return(
        <div className={classes} onClick={props.check?
            doNothing:
            ()=>props.answerAQuestion(props.qId, props.opt.id)}>
                {props.opt.option}
        </div>
    )
}