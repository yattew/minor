import Navbar from './components/Navbar';
import styles from './css/app.module.css';
import { BrowserRouter, Route, Routes } from "react-router-dom";
import SearchPage from './pages/SearchPage';

function App() {
  return (
    <>
      <Navbar />
      <div className={styles.app}>
        <BrowserRouter>
          <Routes>
            <Route path='/' element={<SearchPage />}></Route>
          </Routes>
        </BrowserRouter>
      </div>
    </>
  );
}

export default App;
