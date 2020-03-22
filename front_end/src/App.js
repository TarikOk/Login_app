import React from 'react';
import './App.css';


class App extends React.Component {
  render() {
    return (
      React.createElement('div', {className: 'App'}, React.createElement('h1', null, 'Hello World'))
    );
  };
}

//function App() {
//  return (
//    <div className="App">
//      <h1> Hello World</h1>
//    </div>
//  );
//  return React.createElement('div', {className: 'App'}, React.createElement('h1', null, 'Hello World'));
//}

export default App;
