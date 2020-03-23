import React from 'react';
import './App.css';
import {TextField} from '@material-ui/core/';
import { makeStyles } from '@material-ui/core/styles';
import {Button} from '@material-ui/core/';

const useStyles = makeStyles(theme => ({
  root: {
    '& .MuiTextField-root': {
      margin: theme.spacing(1),
      width: '300px',
    },
  },
  border: {
    width: '315px; height: 350px',
    borderRadius: '15px',
    backgroundColor: '#B0E0E6',
    display: 'inline-block',
    marginLeft: "10%",
    marginTop: "200px",
    padding: '30px',
    opacity: '0.7'
  },
  button: {
    '& > *': {
      margin: theme.spacing(1),
      padding: '15px',
      marginTop: '10px',
      width: '300px; height: 55px',
    },
  },
}));



export default function FormRegistr() {
  const classes = useStyles();
    return (
      <div className={classes.border}>
      <form className={classes.root} noValidate autoComplete="off">
        <div>
          <TextField 
            id="filled-login" 
            label="Login" 
            type="login" 
            variant="filled" />
        </div>
        <div>
          <TextField 
            id="filled-login" 
            label="Email" 
            type="email" 
            variant="filled" />
        </div>
        <div>
          <TextField
            id="filled-password"
            label="Password"
            name="password"
            type="password"
            autoComplete="current-password"
            variant="filled"
          />
        </div>
        <div className={classes.button}>
          <Button variant="contained" color="primary">Registration</Button>
          <Button variant="outlined" color="primary">I have account</Button>
        </div>
      </form>
      </div>
    );
  };





//function App() {
//  return (
//    <div className="App">
//      <h1> Hello World</h1>
//    </div>
//  );
//  return React.createElement('div', {className: 'App'}, React.createElement('h1', null, 'Hello World'));
//}