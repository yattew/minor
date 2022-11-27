import Navbar from './components/Navbar';
import styles from './css/app.module.css';
import { BrowserRouter, Route, Routes } from "react-router-dom";
import HomePage from './pages/home';
import ResultPage from './pages/Result';
import { LearningModeProvider } from './Contexts';
// import ResultPage

function App() {
  return (
    <>
      <LearningModeProvider>
        <BrowserRouter>

          <Navbar />
          <div className={styles.app}>
            <Routes>
              <Route path='/' element={<HomePage />}></Route>
              <Route path='/result/:item' element={<ResultPage />}></Route>
            </Routes>
          </div>
        </BrowserRouter>
      </LearningModeProvider>
    </>
  );
}

export default App;
