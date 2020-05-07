import React , { Component } from 'react';


class ViewMatch extends Component{

    render(){

        const {data} = this.props
        console.log(data)
        return(
            <div>
                    <p>
                        here is component of react
                    </p>
            </div>
        );
    }

}

export default ViewMatch;