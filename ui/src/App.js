import Navbar from './components/Navbar';
import styles from './css/app.module.css';
import { BrowserRouter, Route, Routes } from "react-router-dom";
import HomePage from './pages/home';

function App() {
  return (
    <>
      <Navbar />
      <div className={styles.app}>
        <BrowserRouter>
          <Routes>
            <Route path='/' element={<HomePage />}></Route>
          </Routes>
        </BrowserRouter>
      </div>
    </>
  );
}

export default App;
