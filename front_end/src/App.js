import React from 'react';
import './App.css';
import FormLogin from './FormLogin';
//import FormRegistr from './FormRegistr';



class App extends React.Component {

  userReg = async () => {
    const reg_url = await
    fetch(`http://127.0.0.1:8000/auth/users/`);
    const data = await reg_url.json();
    console.log(data);
  };

  userLogin = async () => {
    const login_url = await
    fetch(`http://127.0.0.1:8000/auth/token/create/`);
    const data = await login_url.json();
    console.log(data);
  };



  render() {
    return (
      <div>
        <FormLogin />
      </div>
    );
  };
}

export default App;


//function App() {
//  return (
//    <div className="App">
//      <h1> Hello World</h1>
//    </div>
//  );
//  return React.createElement('div', {className: 'App'}, React.createElement('h1', null, 'Hello World'));
//}