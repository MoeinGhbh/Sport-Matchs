import React , { Component } from 'react';


class ViewMatch extends Component{

    render(){

        const {title,state, team,tournament,winner,score} = this.props
        return(
            <div>
                    <p>
                        here is component of react
                    </p>
                   <div>
                            <div> {title} </div>
                            <div> {state} </div>
                            <div> {team} </div>
                            <div> {tournament} </div>
                            <div> {winner} </div>
                            <div> {score} </div>
                    </div>
            </div>
        );
    }

}

export default ViewMatch;