import React , { Component } from 'react';
import "./style.css"


class ViewMatch extends Component{

    render(){

        const {mydata} = this.props
        console.log(mydata,'this is my view detailes')

      
        // console.log(mydata["Team"])

        return(
            <div>
                   

                    <table className="tbl">
                        <tr>

                            <td>
                                      <label>Team:  </label>
                            </td>
                            <td>
                                        <label> {mydata["Team"]} </label>
                            </td>

                            <td>
                                      <label>Tttle:  </label>
                            </td>
                            <td>
                                        <label> {mydata["title"]} </label>
                            </td>

                            <td>
                                      <label>state:  </label>
                            </td>
                            <td>
                                        <label> {mydata["state"]} </label>
                            </td>

                            <td>
                                      <label>tournament_name:  </label>
                            </td>
                            <td>
                                        <label> {mydata["tournament_name"]} </label>
                            </td>

                            <td>
                                      <label>winner:  </label>
                            </td>
                            <td>
                                        <label> {mydata["winner"]} </label>
                            </td>


                            <td>
                                      <label>score:  </label>
                            </td>
                            <td>
                                        <label> {mydata["score"]} </label>
                            </td>




                        </tr>
                    </table>

                  
                    
                  
            </div>
        );
    }

}

export default ViewMatch;