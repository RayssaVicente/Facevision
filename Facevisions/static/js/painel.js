function generateCalendar() {
            const grid = document.getElementById('calendarGrid');
            const monthName = document.getElementById('monthName');
            const now = new Date();
            const currentMonth = now.getMonth();
            const currentYear = now.getFullYear();
            const today = now.getDate();

            const monthLabels = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"];
            monthName.innerText = `${monthLabels[currentMonth]} ${currentYear}`;

            const firstDay = new Date(currentYear, currentMonth, 1).getDay();
            const daysInMonth = new Date(currentYear, currentMonth + 1, 0).getDate();

            grid.innerHTML = "";

            // Dias vazios
            for (let i = 0; i < firstDay; i++) {
                const emptyDiv = document.createElement("div");
                emptyDiv.classList.add("calendar-day", "empty");
                grid.appendChild(emptyDiv);
            }

            // Dias do mês
            for (let day = 1; day <= daysInMonth; day++) {
                const dayDiv = document.createElement("div");
                dayDiv.classList.add("calendar-day");
                dayDiv.innerText = day;

                if (day === today) dayDiv.classList.add("today");

                grid.appendChild(dayDiv);
            }
        }
        document.addEventListener('DOMContentLoaded', generateCalendar);