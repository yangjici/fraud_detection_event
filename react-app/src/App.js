import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import 'whatwg-fetch';

class App extends Component {
  constructor(props){
    super(props);
    this.getall = this.getall.bind(this);
    this.state = {records: []};
  }

  componentDidMount(){
    setInterval(() => {
      this.getall();
    }, 500);
  }

  getall(){
    fetch('http://52.53.197.242:3333/getall')
    .then((response) => {
      return response.json()
    }).then((json) => {
        this.setState({records: json})
        console.log('parsed json', json[0].name);
    }).catch((ex) => {
      console.log('parsing failed', ex);
    })
  }

  render() {
    return (
      <div className="App">
          <h1>Prediction Engine</h1>
          <table className="table table-striped">
              <thead>
                  <tr>
                      <th>Name</th>
                      <th>Venue</th>
                      <th>State</th>
                      <th>Prediction</th>
                      <th>Probability</th>
                  </tr>
              </thead>
              <tbody>
                {
                    this.state.records.map((r, i) => {
                        return (
                            <tr key={i}>
                                <td>{r.name}</td>
                                <td>{r.venue}</td>
                                <td>{r.state}</td>
                                <td>{r.prediction}</td>
                                <td>{r.probability.toFixed(3)}</td>
                            </tr>
                        );
                    })
                }
              </tbody>
          </table>
      </div>
    );
  }
}

export default App;
