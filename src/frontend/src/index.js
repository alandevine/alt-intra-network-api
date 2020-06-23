import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import * as serviceWorker from './serviceWorker';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import Dashboard from './routes/Dashboard';
import Settings from './routes/Settings';
import Statistics from './routes/Statistics';
import 'bootstrap/dist/css/bootstrap.min.css';

ReactDOM.render(
  <BrowserRouter>
      <Switch>
        <Route path="/" component={Dashboard} exact />
        <Route path="/statistics" component={Statistics} />
        <Route path="/settings" component={Settings} />
      </Switch>
  </BrowserRouter>,
  document.getElementById('root')
);

// ReactDOM.render(<Dashboard />, document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
